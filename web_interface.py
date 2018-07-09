import sys

from flask import Flask, jsonify

from search_corpus import SearchEngineFromFile


app = Flask(__name__)


@app.route("/search/<query>")
def qiuck_search(query):
    search_engine = SearchEngineFromFile.create(sys.argv[1])
    words = search_engine.get_hits_for_letters(query)

    return jsonify([w.value for w in words])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Erro: please enter the titles file path!')

    else:
        app.run()
