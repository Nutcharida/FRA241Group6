from pyramid.httpexceptions import HTTPFound
from pyramid.view import (
    forbidden_view_config,
    view_config,
)
from ..models import User,Project

@view_config(route_name = 'recommend',renderer = '../templates/InterestProject.pt')
def view_recommend_project(request):
    project_id = request.matchdict["project_id"]
    project = request.db_session.query(Project).filter_by(id = project_id).first()
    dict2return = dict(alert = "")
    if  project.is_recommend is None  :
        dict2return["alert"] = "Project is not exist or Project is not recommended."
    elif project.is_recommend == "F":
        dict2return["alert"] = "Project is not exist or Project is not recommended."
    dict2return.update(project = project)
    return dict2return
