// https://leetcode.com/problems/course-schedule-iii/submissions/949537368/

/**
 * @param {number[][]} courses
 * @return {number}
 */
const scheduleCourse = (courses) => {
    courses.sort((a, b) => a[1] - b[1])

    const takenCourses = new MaxPriorityQueue()
    let totalDuration = 0

    for (const [ duration, lastDay ] of courses) {
        if (totalDuration + duration <= lastDay) {
            takenCourses.enqueue(duration)
            totalDuration += duration
        }
        else if (!takenCourses.isEmpty() && takenCourses.front().element > duration) {
            totalDuration -= takenCourses.dequeue().element
            takenCourses.enqueue(duration)
            totalDuration += duration
        }
    }

    return takenCourses.size()
}
