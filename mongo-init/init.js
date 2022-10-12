let dbName = "tavern"
let collName = "scrolls"
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

db.createCollection(collName, { capped: false });
