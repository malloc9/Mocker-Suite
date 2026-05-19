import cors from "cors";
import dotenv from "dotenv";
import type { Request, Response } from "express";
import express from "express";

dotenv.config();

const app = express();
const PORT = process.env.PORT || 3001;

// Middleware
app.use(cors());
app.use(express.json());

// Basic route
app.get("/", (_req: Request, res: Response) => {
	res.json({ message: "Hello from Mocker Suite API!" });
});

// Start server
app.listen(PORT, () => {
	console.log(`Server is running on port ${PORT}`);
});
