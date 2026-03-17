from fastapi import FastAPI
from api.dal import get_analysis_of_collection_sources, get_finding_new_targets, get_identifying_awakened_sleeping_cells, get_quality_goal_shift_alert, get_visualization_of_a_target_trajectory
from db.connect import connect_to_db

conn = connect_to_db()
app = FastAPI()

@app.get("/q1/Quality_goal_shift_alert")
def quality_goal_shift_alert():
    return get_quality_goal_shift_alert()


@app.get("/q2/Analysis_of_collection_sources")
def analysis_of_collection_sources():
    return get_analysis_of_collection_sources()


@app.get("/q3/Finding_new_targets")
def finding_new_targets():
    return get_finding_new_targets()


@app.get("/q4/Identifying_awakened_sleeping_cells")
def identifying_awakened_sleeping_cells():
    return get_identifying_awakened_sleeping_cells()


@app.get("/q5/Visualization_of_a_target_trajectory/{entity_id}")
def visualization_of_a_target_trajectory(entity_id):
    return get_visualization_of_a_target_trajectory(entity_id)
    

