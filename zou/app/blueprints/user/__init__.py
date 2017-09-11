from flask import Blueprint
from zou.app.utils.api import configure_api_from_blueprint

from .resources import (
    AssetTasksResource,
    AssetTypeAssetsResource,
    OpenProjectsResource,
    ProjectSequencesResource,
    ProjectAssetTypesResource,
    SequenceShotsResource,
    ShotTasksResource
)

routes = [
    ("/data/user/assets/<asset_id>/tasks", AssetTasksResource),
    ("/data/user/shots/<shot_id>/tasks", ShotTasksResource),
    ("/data/user/projects/open", OpenProjectsResource),
    ("/data/user/projects/<project_id>/asset-types", ProjectAssetTypesResource),
    ("/data/user/projects/<project_id>/asset-types/<asset_type_id>/assets",
     AssetTypeAssetsResource),
    ("/data/user/projects/<project_id>/sequences", ProjectSequencesResource),
    ("/data/user/sequences/<sequence_id>/shots", SequenceShotsResource),
]

blueprint = Blueprint("user", "user")
api = configure_api_from_blueprint(blueprint, routes)