/* EndlessOS - a GTK+ engine
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

#ifndef __ENDLESSOS_UTILS_H__
#define __ENDLESSOS_UTILS_H__

enum {
  SIDE_LEFT   = 1,
  SIDE_BOTTOM = 1 << 1,
  SIDE_RIGHT  = 1 << 2,
  SIDE_TOP    = 1 << 3,
  SIDE_ALL    = 0xF
};

void
_cairo_round_rectangle_sides (cairo_t          *cr,
                              gdouble           radius,
                              gdouble           x,
                              gdouble           y,
                              gdouble           width,
                              gdouble           height,
                              guint             sides,
                              GtkJunctionSides  junction);

#endif /* __ENDLESSOS_UTILS_H__ */
