const {} = require('../database')

exports.Genre = {
    courses: (parent, args, context) => {
        const genreId = parent.id;
        return allCourses.filter(item => item.genreId === genreId);
    }
}