from database import get_db_connection


def get_properties(filters):
    """
    Gets a list of database properties according to the provided filters.

    Args:
        filters (dict): filters to select properties (city, status, year built).

    Returns:
        list: List of properties that meet the specified criteria.
    """
    conn = get_db_connection()
    query = """
    SELECT DISTINCT 
        p.address, 
        p.city, 
        p.price, 
        p.description,
        s.name AS status_name
    FROM 
        property p
    JOIN 
        status_history sh ON p.id = sh.property_id
    JOIN 
        status s ON sh.status_id = s.id
    WHERE 
        s.name IN ('pre_venta', 'en_venta', 'vendido')
        AND sh.property_id IN (
            SELECT 
                property_id
            FROM 
                status_history sh2
            JOIN 
                status s2 ON sh2.status_id = s2.id
            WHERE 
                s2.name IN ('pre_venta', 'en_venta', 'vendido')
            GROUP BY 
                sh2.property_id
            HAVING 
                MAX(s2.id) = sh.status_id
        )
    """

    filter_conditions = []
    params = []

    if 'city' in filters:
        filter_conditions.append("p.city = %s")
        params.append(filters['city'])
    if 'status' in filters:
        filter_conditions.append("s.name = %s")
        params.append(filters['status'])
    if 'year' in filters:
        filter_conditions.append("p.year = %s")
        params.append(filters['year'])

    if filter_conditions:
        query += " AND " + " AND ".join(filter_conditions)

    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, params)
    properties = cursor.fetchall()
    cursor.close()
    conn.close()

    return properties


