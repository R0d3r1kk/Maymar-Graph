from api import app, db
from ariadne import (
    load_schema_from_path,
    make_executable_schema,
    graphql_sync,
    snake_case_fallback_resolvers,
    ObjectType,
)
from ariadne.explorer import ExplorerGraphiQL
from flask import request, jsonify
from api.mutations import create_user_resolver
from api.queries import (
    get_users_resolver,
    get_user_resolver,
    get_users_types_resolver,
    get_table_types_resolver,
    get_zones_resolver,
)

query = ObjectType("Query")
mutation = ObjectType("Mutation")

query.set_field("getUsers", get_users_resolver)
query.set_field("getUserById", get_user_resolver)
query.set_field("getUserTypes", get_users_types_resolver)
query.set_field("getTableTypes", get_table_types_resolver)
query.set_field("getZones", get_zones_resolver)

mutation.set_field("createUser", create_user_resolver)
type_defs = load_schema_from_path("./schema.gql")
schema = make_executable_schema(type_defs, query, mutation, snake_case_fallback_resolvers)

explorer_html = ExplorerGraphiQL().html(None)


@app.route("/graphql", methods=["GET"])
def graphql_explorer():
    # On GET request serve the GraphQL explorer.
    # You don't have to provide the explorer if you don't want to
    # but keep on mind this will not prohibit clients from
    # exploring your API using desktop GraphQL explorer app.
    return explorer_html, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    # GraphQL queries are always sent as POST
    data = request.get_json()

    # Note: Passing the request to the context is optional.
    # In Flask, the current request is always accessible as flask.request
    success, result = graphql_sync(
        schema, data, context_value={"request": request}, debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code


# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
    # Runs the Flask application only if the main.py file is being run.
    app.run()
