import path from "node:path";
import Database from "better-sqlite3";

const DB_PATH = path.join(__dirname, "..", "..", "data", "mocks.db");
const db = new Database(DB_PATH);
db.pragma("journal_mode = WAL");
db.pragma("foreign_keys = ON");
export default db;
