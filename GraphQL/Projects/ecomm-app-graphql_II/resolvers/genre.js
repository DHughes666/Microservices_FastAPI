exports.Genre = {
    courses: (parent, args, context) => {
        const courses = context.allCourses
        const genreId = parent.id;
        return courses.filter(item => item.genreId === genreId);
    }
}