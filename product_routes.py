from flask import request, jsonify, Blueprint,send_file,Response
from pytube import Search
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))

parent = os.path.dirname(current)

sys.path.append(parent)

# importing
product_route = Blueprint('product_route', __name__,url_prefix="/")


@product_route.route('/yt/search', methods=['GET'])
def get_search_results():
  keywords = request.args.get('keywords')
  search = Search(keywords)
  
  vidObjList = []
  for v in search.results:
    vidObj = {"title": v.title, "thumbnail": v.thumbnail_url, "url":v.watch_url}
    vidObjList.append(vidObj)
  resp = jsonify(vidObjList)
  return resp





