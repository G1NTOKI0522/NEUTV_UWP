# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import web
import sqlite3

from Utils import DBUtils, FileUtils
from Models import Comment

class DownloadComment:
    def GET(self):
        return None

    def POST(self):
        post = web.input()
        beg_date = post.get('beg_date')
        end_date = post.get('end_date')

        for key, val in post.items():
            print(key, val)

        conn = DBUtils.get_connection()
        comment_list = Comment.query_by_period(conn, beg_date, end_date)
        DBUtils.release_connection(conn)
        
        return FileUtils.generate_comment_file(comment_list)
