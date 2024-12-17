from flask import Flask, jsonify

from api.config import get_logger


_logger = get_logger(logger_name=__name__)


def create_app(*, config_object) -> Flask:
    """Create a flask app instance."""

    flask_app = Flask('ml_api')
    flask_app.config.from_object(config_object)

    # Route pour l'URL racine `/`
    @flask_app.route("/")
    def home():
        return jsonify({"message": "Welcome to the API!"}), 200

    # import blueprints
    from api.controller import prediction_app
    flask_app.register_blueprint(prediction_app)
    _logger.debug('Application instance created')

    return flask_app
