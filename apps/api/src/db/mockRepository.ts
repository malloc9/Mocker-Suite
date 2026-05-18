import db from "./connection";

export interface Mock {
	id: string;
	method: string;
	path: string;
	response_status: number;
	response_body: string | null;
	response_headers: string | null;
	description: string | null;
	is_active: number;
	created_at: string;
	updated_at: string;
}

export function createMock(
	mock: Omit<Mock, "id" | "created_at" | "updated_at">,
): string {
	const id = crypto.randomUUID();
	const now = new Date().toISOString();
	db.prepare(`
    INSERT INTO mocks (id, method, path, response_status, response_body, response_headers, description, is_active, created_at, updated_at)
    VALUES (@id, @method, @path, @response_status, @response_body, @response_headers, @description, @is_active, @created_at, @updated_at)
  `).run({
		id,
		method: mock.method,
		path: mock.path,
		response_status: mock.response_status,
		response_body: mock.response_body ?? null,
		response_headers: mock.response_headers ?? null,
		description: mock.description ?? null,
		is_active: mock.is_active ?? 1,
		created_at: now,
		updated_at: now,
	});
	return id;
}

export function findMockById(id: string): Mock | undefined {
	const row = db.prepare("SELECT * FROM mocks WHERE id = @id").get({ id });
	return row as Mock | undefined;
}

export function findMocks(filters: Partial<Mock> = {}): Mock[] {
	const conditions = Object.keys(filters)
		.map((key) => `${key} = @${key}`)
		.join(" AND ");
	const sql = conditions
		? `SELECT * FROM mocks WHERE ${conditions}`
		: "SELECT * FROM mocks";
	const rows = db.prepare(sql).all(filters);
	return rows as Mock[];
}

export function updateMock(id: string, updates: Partial<Mock>): boolean {
	const now = new Date().toISOString();
	const keys = Object.keys(updates);
	if (keys.length === 0) return false;

	const setClause = keys.map((key) => `${key} = @${key}`).join(", ");
	const sql = `
    UPDATE mocks
    SET ${setClause}, updated_at = @updated_at
    WHERE id = @id
  `;

	const result = db.prepare(sql).run({
		...updates,
		updated_at: now,
		id,
	});

	return result.changes > 0;
}

export function deleteMock(id: string): boolean {
	const result = db.prepare("DELETE FROM mocks WHERE id = @id").run({ id });
	return result.changes > 0;
}
