Analyze the Apache-style access log at /app/access.log and write the summary to /app/report.json. Do not modify the input log.

1. Create /app/report.json.
2. The file must contain a valid JSON object with exactly three fields: total_requests as an integer, unique_ips as an integer, and top_path as a string.
3. total_requests must equal the number of non-empty request records in /app/access.log.
4. unique_ips must equal the number of distinct client IP addresses in the first field of the log records.
5. top_path must equal the request path that occurs most often in the quoted HTTP request lines, counting all HTTP methods.

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.
