let dbName = "tavern"
let user = "root"
let pwd = "root"

let collName = "scrolls"


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

db.createCollection(collName , { capped: false });
