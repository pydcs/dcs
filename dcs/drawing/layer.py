from dataclasses import dataclass
from typing import Any, Dict, List, Union

from dcs.drawing.drawing import Drawing, LineStyle, Rgba
from dcs.drawing.icon import Icon, StandardIcon
from dcs.drawing.line import LineDrawing, LineMode
from dcs.drawing.polygon import (
    PolygonMode,
    Circle,
    Rectangle,
    Oval,
    FreeFormPolygon,
    Arrow,
)
from dcs.drawing.text_box import TextBox
from dcs.mapping import Point


@dataclass
class Layer:
    visible: bool
    name: str
    objects: List[Drawing]

    def load_from_dict(self, data):
        self.visible = data["visible"]
        self.name = data["name"]

        for object_index in sorted(data["objects"].keys()):
            object_data = data["objects"][object_index]
            object = self.load_drawing_from_data(object_data)
            self.objects.append(object)

    def dict(self):
        d = {}
        d["visible"] = self.visible
        d["name"] = self.name

        d["objects"] = {}
        i = 1
        for object in self.objects:
            d["objects"][i] = object.dict()
            i += 1

        return d

    def load_drawing_from_data(self, object_data: Dict[str, Any]) -> Drawing:
        # TODO: Maybe move this stuff into the classes and load_from_dict?

        prim_type = object_data["primitiveType"]
        visible = object_data["visible"]
        color = Rgba.from_color_string(object_data["colorString"])
        layer_name = object_data["layerName"]
        name = object_data["name"]
        mapX: float = object_data["mapX"]
        mapY: float = object_data["mapY"]
        position = Point(mapX, mapY)

        if prim_type == "Line":
            closed = object_data["closed"]
            line_thickness = object_data["thickness"]
            line_style = LineStyle(object_data["style"])
            line_mode = LineMode(object_data["lineMode"])
            points = self.load_points_from_data(object_data["points"])
            return LineDrawing(
                visible,
                position,
                name,
                color,
                layer_name,
                closed,
                line_thickness,
                line_style,
                line_mode,
                points,
            )
        elif prim_type == "Icon":
            file = object_data["file"]
            scale = object_data["scale"]
            angle = object_data["angle"]
            return Icon(visible, position, name, color, layer_name, file, scale, angle)
        elif prim_type == "Polygon":
            polygon_mode = PolygonMode(object_data["polygonMode"])
            fill = Rgba.from_color_string(object_data["fillColorString"])
            line_thickness = object_data["thickness"]
            line_style = LineStyle(object_data["style"])

            if polygon_mode == PolygonMode.Circle:
                radius = object_data["radius"]
                return Circle(
                    visible,
                    position,
                    name,
                    color,
                    layer_name,
                    fill,
                    line_thickness,
                    line_style,
                    radius,
                )
            elif polygon_mode == PolygonMode.Oval:
                radius1 = object_data["r1"]
                radius2 = object_data["r2"]
                angle = object_data["angle"]
                return Oval(
                    visible,
                    position,
                    name,
                    color,
                    layer_name,
                    fill,
                    line_thickness,
                    line_style,
                    radius1,
                    radius2,
                    angle,
                )
            elif polygon_mode == PolygonMode.Rectangle:
                width = object_data["width"]
                height = object_data["height"]
                angle = object_data["angle"]
                return Rectangle(
                    visible,
                    position,
                    name,
                    color,
                    layer_name,
                    fill,
                    line_thickness,
                    line_style,
                    width,
                    height,
                    angle,
                )
            elif polygon_mode == PolygonMode.Free:
                points = self.load_points_from_data(object_data["points"])
                return FreeFormPolygon(
                    visible,
                    position,
                    name,
                    color,
                    layer_name,
                    fill,
                    line_thickness,
                    line_style,
                    points,
                )
            elif polygon_mode == PolygonMode.Arrow:
                angle = object_data["angle"]
                length = object_data["length"]
                points = self.load_points_from_data(object_data["points"])
                return Arrow(
                    visible,
                    position,
                    name,
                    color,
                    layer_name,
                    fill,
                    line_thickness,
                    line_style,
                    length,
                    angle,
                    points,
                )
        elif prim_type == "TextBox":
            text = object_data["text"]
            font_size = object_data["fontSize"]
            font = object_data["font"]
            border_thickness = object_data["borderThickness"]
            fill = Rgba.from_color_string(object_data["fillColorString"])
            angle = object_data["angle"]
            return TextBox(
                visible,
                position,
                name,
                color,
                layer_name,
                text,
                font_size,
                font,
                border_thickness,
                fill,
                angle,
            )
        raise RuntimeError(f"Unknown primitive type for layer: {prim_type}")

    def load_points_from_data(self, points_data) -> List[Point]:
        points: List[Point] = []
        for point_index in sorted(points_data.keys()):
            x = points_data[point_index]["x"]
            y = points_data[point_index]["y"]
            points.append(Point(x, y))
        return points

    def add_drawing(self, drawing: Drawing):
        drawing.layer_name = self.name  # Should we do this?
        self.objects.append(drawing)

    def remove_drawing_by_name(self, name: str):
        raise NotImplementedError()

    def remove_drawing(self, drawing: Drawing):
        self.objects.remove(drawing)

    def add_line_segment(
        self,
        position: Point,
        end_point: Point,
        color=Rgba(255, 0, 0, 255),
        line_thickness=8,
        line_style=LineStyle.Solid,
    ) -> LineDrawing:
        points = [Point(0, 0), end_point]
        drawing = LineDrawing(
            True,
            position,
            "A line",
            color,
            self.name,
            False,
            line_thickness,
            line_style,
            LineMode.Segment,
            points,
        )
        self.add_drawing(drawing)
        return drawing

    def add_line_segments(
        self,
        position: Point,
        points: List[Point],
        color=Rgba(255, 0, 0, 255),
        line_thickness=8,
        line_style=LineStyle.Solid,
        closed=False,
    ) -> LineDrawing:
        drawing = LineDrawing(
            True,
            position,
            "A line",
            color,
            self.name,
            closed,
            line_thickness,
            line_style,
            LineMode.Segments,
            points,
        )
        self.add_drawing(drawing)
        return drawing

    def add_line_freeform(
        self,
        position: Point,
        points: List[Point],
        color=Rgba(255, 0, 0, 255),
        line_thickness=8,
        line_style=LineStyle.Solid,
        closed=False,
    ) -> LineDrawing:
        drawing = LineDrawing(
            True,
            position,
            "A line",
            color,
            self.name,
            closed,
            line_thickness,
            line_style,
            LineMode.Free,
            points,
        )
        self.add_drawing(drawing)
        return drawing

    def add_icon(
        self, position: Point, file: Union[str, StandardIcon], scale=1.0, color=Rgba(255, 0, 0, 255)
    ) -> Icon:
        if isinstance(file, StandardIcon):
            file_str = file.value
        else:
            file_str = file

        drawing = Icon(True, position, "An icon", color, self.name, file_str, scale, 0)
        self.add_drawing(drawing)
        return drawing

    def add_text_box(
        self,
        position: Point,
        text: str,
        color=Rgba(255, 0, 0, 255),
        fill=Rgba(255, 0, 0, 60),
        font_size=20,
        font="DejaVuLGCSansCondensed.ttf",
        border_thickness=2,
        angle=0,
    ) -> TextBox:
        drawing = TextBox(
            True,
            position,
            "A text box",
            color,
            self.name,
            text,
            font_size,
            font,
            border_thickness,
            fill,
            angle,
        )
        self.add_drawing(drawing)
        return drawing

    def add_circle(
        self,
        position: Point,
        radius: float,
        color=Rgba(255, 0, 0, 255),
        fill=Rgba(255, 0, 0, 60),
        line_thickness=8,
        line_style=LineStyle.Solid,
    ) -> Circle:
        drawing = Circle(
            True,
            position,
            "A circle",
            color,
            self.name,
            fill,
            line_thickness,
            line_style,
            radius,
        )
        self.add_drawing(drawing)
        return drawing

    def add_oval(
        self,
        position: Point,
        radius1: float,
        radius2: float,
        color=Rgba(255, 0, 0, 255),
        fill=Rgba(255, 0, 0, 60),
        line_thickness=8,
        line_style=LineStyle.Solid,
        angle=0,
    ) -> Oval:
        drawing = Oval(
            True,
            position,
            "An oval",
            color,
            self.name,
            fill,
            line_thickness,
            line_style,
            radius1,
            radius2,
            angle,
        )
        self.add_drawing(drawing)
        return drawing

    def add_rectangle(
        self,
        position: Point,
        width: float,
        height: float,
        color=Rgba(255, 0, 0, 255),
        fill=Rgba(255, 0, 0, 60),
        line_thickness=8,
        line_style=LineStyle.Solid,
        angle=0,
    ) -> Rectangle:
        drawing = Rectangle(
            True,
            position,
            "A rectangle",
            color,
            self.name,
            fill,
            line_thickness,
            line_style,
            width,
            height,
            angle,
        )
        self.add_drawing(drawing)
        return drawing

    def add_freeform_polygon(
        self,
        position: Point,
        points: List[Point],
        color=Rgba(255, 0, 0, 255),
        fill=Rgba(255, 0, 0, 60),
        line_thickness=8,
        line_style=LineStyle.Solid,
    ) -> FreeFormPolygon:
        drawing = FreeFormPolygon(
            True,
            position,
            "A freeform polygon",
            color,
            self.name,
            fill,
            line_thickness,
            line_style,
            points,
        )
        self.add_drawing(drawing)
        return drawing

    def add_arrow(
        self,
        position: Point,
        angle: float,
        length: float,
        color=Rgba(255, 0, 0, 255),
        fill=Rgba(255, 0, 0, 255),
        line_thickness=8,
        line_style=LineStyle.Solid,
    ) -> Arrow:
        drawing = Arrow(
            True,
            position,
            "An arrow",
            color,
            self.name,
            fill,
            line_thickness,
            line_style,
            length,
            angle,
            Arrow.get_default_arrow_points(),
        )
        self.add_drawing(drawing)
        return drawing

    def add_oblong(
        self,
        p1: Point,
        p2: Point,
        radius: float,
        color=Rgba(255, 0, 0, 255),
        fill=Rgba(255, 0, 0, 60),
        line_thickness=4,
        line_style=LineStyle.Solid,
        resolution=20,
    ) -> FreeFormPolygon:
        hdg_p1_p2 = p1.heading_between_point(p2)
        points: List[Point] = []

        for i in range(0, resolution + 1):
            hdg = hdg_p1_p2 - 90 + i * (180 / resolution)
            points.append(p2.point_from_heading(hdg, radius))

        for i in range(0, resolution + 1):
            hdg = hdg_p1_p2 + 90 + i * (180 / resolution)
            points.append(p1.point_from_heading(hdg, radius))

        # Copy first point and insert last to close the polygon
        points.append(points[0] * 1)

        # Transform points to local coordinates
        startPoint = points[0] * 1  # Copy
        for point in points:
            point.x -= startPoint.x
            point.y -= startPoint.y

        polygon = self.add_freeform_polygon(
            startPoint,
            points,
            color=color,
            fill=fill,
            line_thickness=line_thickness,
            line_style=line_style,
        )
        return polygon
