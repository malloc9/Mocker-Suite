import type { NextFunction, Request, Response } from "express";
import { findMocks } from "../db/mockRepository";

export function mockRouter(req: Request, res: Response, next: NextFunction) {
	const { method, path } = req;

	// Find active mocks matching the method and path
	const mocks = findMocks({ method, path, is_active: 1 });

	if (mocks.length === 0) {
		// No matching mock, continue to next middleware/route
		return next();
	}

	// Use the first matching mock (should be unique due to unique index)
	const mock = mocks[0];

	// Set response status
	res.status(mock.response_status);

	// Set response headers if they exist
	if (mock.response_headers) {
		try {
			const headers = JSON.parse(mock.response_headers);
			Object.entries(headers).forEach(([key, value]) => {
				res.setHeader(key, value);
			});
		} catch (_e) {
			console.error("Failed to parse response_headers JSON:", e);
			// Continue without custom headers
		}
	}

	// Send response body if it exists
	if (mock.response_body !== null && mock.response_body !== undefined) {
		try {
			// Try to parse as JSON to send as JSON
			const parsedBody = JSON.parse(mock.response_body);
			res.json(parsedBody);
		} catch (_e) {
			// If not valid JSON, send as plain text
			res.send(mock.response_body);
		}
	} else {
		// No body to send
		res.send("");
	}
}
