from db.connect import connect_to_db
from students_part_2.DigitalHunter_map import plot_map_with_geometry

conn = connect_to_db()
#1
def get_quality_goal_shift_alert():
    cursor = conn.cursor()
    cursor.execute("""select entity_id, target_name, priority_level, movement_distance_km 
                        from targets 
                        where (priority_level = 1 or priority_level = 2)
                        and movement_distance_km > 5.0;""")
    result = cursor.fetchall()
    cursor.close()
    return result

#2
def get_analysis_of_collection_sources():
    cursor = conn.cursor()
    cursor.execute("""select signal_type, count(signal_type) as count_type
                        from intel_signals
                        group by signal_type
                        order by count(signal_type) desc;""")
    result = cursor.fetchall()
    cursor.close()
    return result

#3
def get_finding_new_targets():
    cursor = conn.cursor()
    cursor.execute("""select entity_id, count(entity_id)as count_reports
                        from intel_signals
                        where priority_level = 99
                        group by entity_id
                        order by count_reports desc
                        limit 3;""")
    result = cursor.fetchall()
    cursor.close()
    return result

#4
def get_identifying_awakened_sleeping_cells():
    cursor = conn.cursor()
    cursor.execute("""select day.entity_id from
                        (select entity_id from intel_signals where distance_from_last = 0 
                        and hour(timestamp) between 8 and 20 
                        group by entity_id) as day
                        join
                        (select entity_id from intel_signals where distance_from_last >= 10 
                        and hour(timestamp) not between 8 and 20 
                        group by entity_id) as night
                        on day.entity_id = night.entity_id;""")
    result = cursor.fetchall()
    cursor.close()
    return result

#5
def get_visualization_of_a_target_trajectory(entity_id):
    cursor = conn.cursor()
    cursor.execute("""select entity_id, reported_lat, reported_lon
                        from intel_signals
                        order by entity_id;""")
    result = cursor.fetchall()
    if result["entity_id"] == entity_id:
        lat = result["reported_lat"]
        lon = result["reported_lon"]
        visual = plot_map_with_geometry(lat, lon)
    cursor.close()
    return visual





