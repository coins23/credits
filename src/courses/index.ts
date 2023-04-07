import type Course from "../Course";
import courses from "./courses.json";

const codeToCourse = new Map<string, Course>();

for (const course of courses) {
  codeToCourse.set(course.code, course);
}

export default codeToCourse;
