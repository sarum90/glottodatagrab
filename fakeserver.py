
import json


class FakeServer(object):
  """Fake Server for use in testing pyglottolog."""

  def __init__(self, num_items):
    """Basic constructor for a fake  server with num_items items in it."""
    self._num_items = num_items
  
  def GetResults(self, start_index, count):
    """Simple interface that responds with the requested URL."""
    result = []
    for i in xrange(count):
      index = i + start_index
      if index >= self._num_items:
        break
      result.append({"properties": { "language": {"id": index} } })
    return json.dumps(
        {"type": "FeatureCollection",
         "properties": {"layer": ""},
         "features": result})

