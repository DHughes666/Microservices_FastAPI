exports.Course = {
    genre: (parent, args, context) => {
        const genres = context.genres
        const genreId = parent.genreId;
        return genres.find(item => item.id === genreId);
    },
    reviews: (parent, args, context) => {
        const reviews = context.reviews
        const { id } = parent;
        return reviews.filter(item => item.courseId === id);
    }
}