# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PipelinePlanner
                                 A QGIS plugin
 Permite al usuario crear una línea y evaluar impactos
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-02-06
        copyright            : (C) 2023 by SyK S.A.
        email                : syksa@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load PipelinePlanner class from file PipelinePlanner.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .pipeline_planner import PipelinePlanner
    return PipelinePlanner(iface)
