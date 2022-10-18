let dbName = "tavern"
let collName = "scrolls"
let collNameTicket = "tickets"
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
db.createCollection(collNameTicket, { capped: false });
