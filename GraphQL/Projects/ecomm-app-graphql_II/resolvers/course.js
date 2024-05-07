exports.Course = {
    genre: (parent, args, context) => {
        const genres = context.genres
        const genreId = parent.genreId;
        return genres.find(item => item.id === genreId);
    }
}