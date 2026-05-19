import { Router } from "express";
import { z } from "zod";
import {
	createMock,
	deleteMock,
	findMockById,
	findMocks,
	updateMock,
} from "../db/mockRepository";

const router = Router();

// Validation schema for mock
const mockSchema = z.object({
	method: z.enum(["GET", "POST", "PUT", "PATCH", "DELETE"]),
	path: z.string(),
	response_status: z.number().int().min(100).max(599).default(200),
	response_body: z.string().optional(),
	response_headers: z.string().optional(),
	description: z.string().optional(),
	is_active: z.number().min(0).max(1).default(1),
});

// POST /api/mocks: Create a new mock configuration
router.post("/", (req, res) => {
	const result = mockSchema.safeParse(req.body);
	if (!result.success) {
		return res
			.status(400)
			.json({ error: "Invalid request body", details: result.error.format() });
	}

	try {
		const id = createMock(result.data);
		res.status(201).json({ id });
	} catch (error) {
		res
			.status(500)
			.json({ error: "Failed to create mock", details: error.message });
	}
});

// GET /api/mocks: List all mock configurations
router.get("/", (_req, res) => {
	try {
		const mocks = findMocks();
		res.json(mocks);
	} catch (error) {
		res
			.status(500)
			.json({ error: "Failed to fetch mocks", details: error.message });
	}
});

// GET /api/mocks/:id: Get a single mock by its ID
router.get("/:id", (req, res) => {
	const { id } = req.params;
	try {
		const mock = findMockById(id);
		if (!mock) {
			return res.status(404).json({ error: "Mock not found" });
		}
		res.json(mock);
	} catch (error) {
		res
			.status(500)
			.json({ error: "Failed to fetch mock", details: error.message });
	}
});

// PUT /api/mocks/:id: Update an existing mock configuration
router.put("/:id", (req, res) => {
	const { id } = req.params;
	const result = mockSchema.partial().safeParse(req.body);
	if (!result.success) {
		return res
			.status(400)
			.json({ error: "Invalid request body", details: result.error.format() });
	}

	try {
		const success = updateMock(id, result.data);
		if (!success) {
			return res.status(404).json({ error: "Mock not found" });
		}
		res.json({ message: "Mock updated successfully" });
	} catch (error) {
		res
			.status(500)
			.json({ error: "Failed to update mock", details: error.message });
	}
});

// DELETE /api/mocks/:id: Delete a mock configuration
router.delete("/:id", (req, res) => {
	const { id } = req.params;
	try {
		const success = deleteMock(id);
		if (!success) {
			return res.status(404).json({ error: "Mock not found" });
		}
		res.json({ message: "Mock deleted successfully" });
	} catch (error) {
		res
			.status(500)
			.json({ error: "Failed to delete mock", details: error.message });
	}
});

export default router;
