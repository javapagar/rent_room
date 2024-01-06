from flask import Blueprint

blueprint = Blueprint("health",__name__)

@blueprint.route("/health",methods=["GET"])
def check_health():
    return "All is ok!!"