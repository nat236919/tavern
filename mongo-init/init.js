let dbName = "tavern"
let user = "root"
let pwd = "root"

conn = new Mongo();
db = conn.getDB(dbName)

db.createUser(
    {
        user: user,
        pwd: pwd,
        roles: [
            {
                role: "readWrite",
                db: dbName
            }
        ]
    }
);

db.createCollection('scrolls', { capped: false });
