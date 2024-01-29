print("Starting the database initialization.");

db = new Mongo().getDB("admin");

print("Creating root user.");

db = db.getSiblingDB("admin");

db.createUser({
  user: _getEnv("MONGO_INITDB_ROOT_USERNAME"),
  pwd: _getEnv("MONGO_INITDB_ROOT_PASSWORD"),
  roles: [{ role: "readWrite", db: "myDatabase" }],
});

print("Root user created.");

db.auth({
  user: _getEnv("MONGO_INITDB_ROOT_USERNAME"),
  pwd: _getEnv("MONGO_INITDB_ROOT_PASSWORD"),
});

db = db.getSiblingDB("docker_db");

db.createUser({
  user: _getEnv("MONGO_INITDB_ROOT_USERNAME"),
  pwd: _getEnv("MONGO_INITDB_ROOT_PASSWORD"),
  roles: [
    {
      role: "readWrite",
      db: "docker_db",
    },
  ],
});

print("Database initialization completed.");

function _getEnv(variable) {
  return variable in process.env ? process.env[variable] : "";
}
