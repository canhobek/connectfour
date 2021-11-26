from model.board import Board
from model.player import CircularPlayerIterator
from model.tile import Tile

from flask import Flask, render_template, request, redirect, url_for


class WebView(Flask):
    def __init__(self, board: Board, players):
        super(WebView, self).__init__(__name__)
        self._board = board

        self._player_iter = CircularPlayerIterator(players)

        self.template_folder = "../../view/web/templates"
        self.static_folder = "../../view/web/static"

        self.route("/")(self.display_board)
        self.route("/play/<int:column>", methods=["GET"])(self.play)

        self.debug = True

    def display_board(self):
        return render_template("board_view.html", board=list(reversed(self._board.get_board())))

    def play(self, column):
        if request.method == "GET":
            player = next(self._player_iter)
            self._board.play(column, tile=player.tile)
            return redirect(url_for("display_board"))
