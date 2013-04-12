/* Adwaita - a GTK+ engine
 *
 * Copyright (C) 2011 Carlos Garnacho <carlosg@gnome.org>
 * Copyright (C) 2011 Red Hat, Inc.
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 * 
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	 See the GNU
 * Lesser General Public License for more details.
 * 
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
 *
 * Authors: Carlos Garnacho <carlosg@gnome.org>
 *          Cosimo Cecchi <cosimoc@gnome.org>
 *
 * Project contact: <gnome-themes-list@gnome.org>
 */

#include <gtk/gtk.h>
#include <gmodule.h>
#include <math.h>
#include <cairo-gobject.h>

#ifdef GDK_WINDOWING_X11
#include <gdk/gdkx.h>
#endif

#include "adwaita_utils.h"

#define ADWAITA_NAMESPACE "adwaita"

typedef struct _AdwaitaEngine AdwaitaEngine;
typedef struct _AdwaitaEngineClass AdwaitaEngineClass;

struct _AdwaitaEngine
{
  GtkThemingEngine parent_object;

  guint wm_watch_id;
  GtkCssProvider *fallback_provider;
};

struct _AdwaitaEngineClass
{
  GtkThemingEngineClass parent_class;
};

#define ADWAITA_TYPE_ENGINE		 (adwaita_engine_get_type ())
#define ADWAITA_ENGINE(object)		 (G_TYPE_CHECK_INSTANCE_CAST ((object), ADWAITA_TYPE_ENGINE, AdwaitaEngine))
#define ADWAITA_ENGINE_CLASS(klass)	 (G_TYPE_CHECK_CLASS_CAST ((klass), ADWAITA_TYPE_ENGINE, AdwaitaEngineClass))
#define ADWAITA_IS_ENGINE(object)	 (G_TYPE_CHECK_INSTANCE_TYPE ((object), ADWAITA_TYPE_ENGINE))
#define ADWAITA_IS_ENGINE_CLASS(klass)	 (G_TYPE_CHECK_CLASS_TYPE ((klass), ADWAITA_TYPE_ENGINE))
#define ADWAITA_ENGINE_GET_CLASS(obj)	 (G_TYPE_INSTANCE_GET_CLASS ((obj), ADWAITA_TYPE_ENGINE, AdwaitaEngineClass))

GType adwaita_engine_get_type	    (void) G_GNUC_CONST;
void  adwaita_engine_register_types (GTypeModule *module);

G_DEFINE_DYNAMIC_TYPE (AdwaitaEngine, adwaita_engine, GTK_TYPE_THEMING_ENGINE)

void
adwaita_engine_register_types (GTypeModule *module)
{
  adwaita_engine_register_type (module);
}

static void
fallback_provider_remove (AdwaitaEngine *self)
{
  GdkScreen *screen;

  if (self->fallback_provider == NULL)
    return;

  screen = gdk_screen_get_default ();
  gtk_style_context_remove_provider_for_screen
    (screen, GTK_STYLE_PROVIDER (self->fallback_provider));
  g_clear_object (&self->fallback_provider);
}

static void
fallback_provider_add (AdwaitaEngine *self)
{
  GFile *resource;
  GtkCssProvider *provider;
  GError *error = NULL;
  GdkScreen *screen;

  if (self->fallback_provider != NULL)
    return;

  resource = g_file_new_for_uri ("resource:///org/gnome/adwaita/gtk-fallback.css");
  provider = gtk_css_provider_new ();
  gtk_css_provider_load_from_file (provider, resource, &error);
  g_object_unref (resource);

  if (error != NULL)
    {
      g_warning ("Can't load fallback CSS resource: %s", error->message);
      g_error_free (error);
      g_object_unref (provider);
      return;
    }

  screen = gdk_screen_get_default ();
  gtk_style_context_add_provider_for_screen
    (screen, GTK_STYLE_PROVIDER (provider), GTK_STYLE_PROVIDER_PRIORITY_THEME);
  self->fallback_provider = provider;
}

static void
adwaita_engine_wm_changed (AdwaitaEngine *self)
{
  gboolean is_fallback = TRUE;

#ifdef GDK_WINDOWING_X11
  const gchar *name;
  GdkScreen *screen = gdk_screen_get_default ();
  if (GDK_IS_X11_SCREEN (screen))
    {
      name = gdk_x11_screen_get_window_manager_name (screen);
      is_fallback = (g_strcmp0 (name, "GNOME Shell") != 0);
    }
#endif

  if (is_fallback)
    fallback_provider_add (self);
  else
    fallback_provider_remove (self);
}

static void
adwaita_engine_finalize (GObject *obj)
{
  AdwaitaEngine *self = ADWAITA_ENGINE (obj);

  if (self->wm_watch_id != 0)
    {
      g_signal_handler_disconnect (gdk_screen_get_default (), self->wm_watch_id);
      self->wm_watch_id = 0;
    }

  fallback_provider_remove (self);

  G_OBJECT_CLASS (adwaita_engine_parent_class)->finalize (obj);
}

static void
adwaita_engine_init (AdwaitaEngine *self)
{
#ifdef GDK_WINDOWING_X11
  GdkScreen *screen = gdk_screen_get_default ();

  if (GDK_IS_X11_SCREEN (screen))
    {
      self->wm_watch_id =
	g_signal_connect_swapped (screen, "window-manager-changed",
				  G_CALLBACK (adwaita_engine_wm_changed), self);
    }
#endif

  adwaita_engine_wm_changed (self);
}

static void
adwaita_engine_render_arrow (GtkThemingEngine *engine,
                             cairo_t          *cr,
                             gdouble           angle,
                             gdouble           x,
                             gdouble           y,
                             gdouble           size)
{
  double line_width;
  GtkStateFlags state;
  GdkRGBA color;

  cairo_save (cr);

  line_width = size / 3.0 / sqrt (2);
  cairo_set_line_width (cr, line_width);
  cairo_set_line_join (cr, CAIRO_LINE_JOIN_ROUND);
  cairo_set_line_cap (cr, CAIRO_LINE_CAP_ROUND);

  cairo_translate (cr, x + size / 2.0, y + size / 2.0);
  cairo_rotate (cr, angle - G_PI_2);
  cairo_translate (cr, size / 4.0, 0);
 
  cairo_scale (cr,
               (size / (size + line_width)),
               (size / (size + line_width)));

  cairo_move_to (cr, -size / 2.0, -size / 2.0);
  cairo_rel_line_to (cr, size / 2.0, size / 2.0);
  cairo_rel_line_to (cr, - size / 2.0, size / 2.0);

  state = gtk_theming_engine_get_state (engine);
  gtk_theming_engine_get_color (engine, state, &color);
  gdk_cairo_set_source_rgba (cr, &color);
  cairo_stroke (cr);

  cairo_restore (cr);
}

static void
adwaita_engine_render_focus (GtkThemingEngine *engine,
                             cairo_t          *cr,
                             gdouble           x,
                             gdouble           y,
                             gdouble           width,
                             gdouble           height)
{
  GdkRGBA *border_color = NULL;
  GtkStateFlags state;
  gint line_width, focus_pad;
  gint border_radius;
  double dashes[2] = { 2.0, 0.2 };
  const GtkWidgetPath *path;
  GtkBorderStyle border_style;

  path = gtk_theming_engine_get_path (engine);
  state = gtk_theming_engine_get_state (engine);
  gtk_theming_engine_get (engine, state,
                          "outline-color", &border_color,
                          "outline-style", &border_style,
                          "outline-offset", &border_radius,
                          NULL);

  gtk_theming_engine_get_style (engine,
                                "focus-line-width", &line_width,
                                "focus-padding", &focus_pad,
                                NULL);

  /* as we render the tab smaller than the whole allocation, we need
   * to recenter and resize the focus on the tab.
   */
  if (gtk_theming_engine_has_class (engine, GTK_STYLE_CLASS_NOTEBOOK) &&
      gtk_theming_engine_has_region (engine, GTK_STYLE_REGION_TAB, NULL))
    {
      y += 3.0;
      height -= 3.0;
    }

  /* the treeview rows don't change allocation when modifying focus-padding,
   * so we have to move the focus ring inside the allocated area manually.
   */
  if (gtk_widget_path_is_type (path, GTK_TYPE_TREE_VIEW))
    {
      x += focus_pad;
      y += focus_pad;
      width -= 2 * focus_pad;
      height -= 2 * focus_pad;
    }

  cairo_save (cr);
  cairo_set_line_width (cr, line_width);

  if (line_width > 1)
    _cairo_round_rectangle_sides (cr, border_radius,
                                  x, y, width, height,
                                  SIDE_ALL, GTK_JUNCTION_NONE);
  else
    _cairo_round_rectangle_sides (cr, border_radius,
                                  x + 0.5, y + 0.5,
                                  width - 1, height - 1,
                                  SIDE_ALL, GTK_JUNCTION_NONE);

  if (border_style == GTK_BORDER_STYLE_DASHED)
    cairo_set_dash (cr, dashes, 1, 0.0);

  if (border_color != NULL)
    gdk_cairo_set_source_rgba (cr, border_color);

  cairo_stroke (cr);
  cairo_restore (cr);

  if (border_color != NULL)
    gdk_rgba_free (border_color);
}

#define NOTEBOOK_TAB_TOP_MARGIN 3.0

static void
draw_tab_shape (cairo_t *cr,
                gdouble curve_width,
                gdouble x,
                gdouble y,
                gdouble width,
                gdouble height)
{
  cairo_move_to (cr, x, height);

  cairo_arc (cr, 
             x + curve_width, y + 3.0,
             2.5,
             G_PI, G_PI + G_PI_2);

  cairo_arc (cr,
             x + width - curve_width, y + 3.0,
             2.5,
             G_PI + G_PI_2, 2 * G_PI);

  cairo_line_to (cr, x + width, height);
}

static void
render_notebook_extension (GtkThemingEngine *engine,
                           cairo_t          *cr,
                           gdouble           x,
                           gdouble           y,
                           gdouble           width,
                           gdouble           height,
                           GtkPositionType   gap_side)
{
  gint tab_curvature, border_width;
  GdkRGBA border_color, background_color;
  GtkStateFlags state;
  gdouble angle = 0;
  cairo_pattern_t *pattern = NULL;
  gboolean is_active;

  gtk_theming_engine_get_style (engine,
                                "tab-curvature", &tab_curvature,
                                NULL);
  state = gtk_theming_engine_get_state (engine);
  gtk_theming_engine_get_background_color (engine, state, &background_color);
  gtk_theming_engine_get_border_color (engine, state, &border_color);
  gtk_theming_engine_get (engine, state,
                          "border-image-source", &pattern,
                          NULL);

  is_active = (state & GTK_STATE_FLAG_ACTIVE);
  border_width = 1.0;

  cairo_save (cr);
  cairo_set_line_width (cr, border_width);

  if (gap_side == GTK_POS_BOTTOM)
    x += border_width / 2;
  else if (gap_side == GTK_POS_TOP)
    x -= border_width / 2;

  if (gap_side == GTK_POS_TOP)
    {
      angle = G_PI;
      cairo_translate (cr, x + width, y + height - NOTEBOOK_TAB_TOP_MARGIN - border_width);
    }
  else
    {
      cairo_translate (cr, x, y + NOTEBOOK_TAB_TOP_MARGIN + border_width);
    }

  cairo_rotate (cr, angle);

  width -= border_width;
  height -= NOTEBOOK_TAB_TOP_MARGIN + border_width;

  /* draw the tab shape and clip the background inside it */
  cairo_save (cr);
  draw_tab_shape (cr, tab_curvature, 
                  0, 0.5,
                  width, is_active ? (height + 1.0) : (height));
  cairo_clip (cr);

  GTK_THEMING_ENGINE_CLASS (adwaita_engine_parent_class)->render_background
    (engine, cr, 0, 0.5,
     width, is_active ? (height + 1.0) : (height));

  cairo_restore (cr);

  /* now draw the border */
  draw_tab_shape (cr, tab_curvature,
                  0, 0,
                  width, height);

  if (pattern && (state & GTK_STATE_FLAG_ACTIVE))
    {
      cairo_scale (cr, width, height);
      cairo_set_source (cr, pattern);
      cairo_scale (cr, 1.0 / width, 1.0 / height);
    }
  else
    {
      gdk_cairo_set_source_rgba (cr, &border_color);
    }

  cairo_stroke (cr);

  if (pattern != NULL)
    cairo_pattern_destroy (pattern);

  cairo_restore (cr);
}

static void
adwaita_engine_render_extension (GtkThemingEngine *engine,
                                 cairo_t          *cr,
                                 gdouble           x,
                                 gdouble           y,
                                 gdouble           width,
                                 gdouble           height,
                                 GtkPositionType   gap_side)
{
  if (gtk_theming_engine_has_class (engine, GTK_STYLE_CLASS_NOTEBOOK) &&
      ((gap_side == GTK_POS_TOP) || (gap_side == GTK_POS_BOTTOM)))
    {
      render_notebook_extension (engine, cr, x, y, width, height, gap_side);
      return;
    }

  GTK_THEMING_ENGINE_CLASS (adwaita_engine_parent_class)->render_extension
    (engine, cr,
     x, y, width, height,
     gap_side);
}

static void
adwaita_engine_class_init (AdwaitaEngineClass *klass)
{
  GtkThemingEngineClass *engine_class = GTK_THEMING_ENGINE_CLASS (klass);
  GObjectClass *oclass = G_OBJECT_CLASS (klass);

  oclass->finalize = adwaita_engine_finalize;

  engine_class->render_arrow = adwaita_engine_render_arrow;
  engine_class->render_focus = adwaita_engine_render_focus;
  engine_class->render_extension = adwaita_engine_render_extension;
}

static void
adwaita_engine_class_finalize (AdwaitaEngineClass *klass)
{
}

G_MODULE_EXPORT void
theme_init (GTypeModule *module)
{
  adwaita_engine_register_types (module);
}

G_MODULE_EXPORT void
theme_exit (void)
{
}

G_MODULE_EXPORT GtkThemingEngine *
create_engine (void)
{
  return GTK_THEMING_ENGINE (g_object_new (ADWAITA_TYPE_ENGINE,
                                           "name", "adwaita",
                                           NULL));
}
