from pykml import parser
import gpxpy
import gpxpy.gpx

# Abre el archivo KML y parsea su contenido
# IMPORTANTE: Reemplaza 'kml/87.kml' con el nombre del archivo KML que deseas convertir
with open('kml/87.kml', 'r') as kml_file:
    kml = parser.parse(kml_file).getroot().Document.Placemark.Polygon.outerBoundaryIs.LinearRing.coordinates

# Crea un nuevo objeto GPX
gpx = gpxpy.gpx.GPX()

# Crea una nueva pista GPX y añádela al objeto GPX
gpx_track = gpxpy.gpx.GPXTrack()
gpx.tracks.append(gpx_track)

# Crea un nuevo segmento de pista GPX y añádelo a la pista GPX
gpx_segment = gpxpy.gpx.GPXTrackSegment()
gpx_track.segments.append(gpx_segment)

# Itera sobre los puntos en el archivo KML
for point in kml.text.split():
    # Divide las coordenadas (están en el formato 'long,lat,alt')
    coordinates = point.split(',')
    # Crea un nuevo punto GPX
    gpx_point = gpxpy.gpx.GPXTrackPoint(
        latitude=float(coordinates[1]),
        longitude=float(coordinates[0]),
        elevation=float(coordinates[2])
    )
    # Añade el punto al segmento de la pista GPX
    gpx_segment.points.append(gpx_point)

# Guarda el objeto GPX en un nuevo archivo
with open('output.gpx', 'w') as gpx_file:
    gpx_file.write(gpx.to_xml())