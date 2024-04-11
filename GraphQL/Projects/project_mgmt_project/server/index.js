const express = require('express');
require('dotenv').config();
const { graphqlHTTP } = require('express-graphql');
const schema = require('./schema/schema');
const dbConnect = require('../config/db');
const port = process.env.PORT || 5000;

const app = express();

dbConnect();

app.use(
    '/graphql',
    graphqlHTTP({
        schema,
        graphiql: process.env.NODE_ENV === 'development'
    })
)




app.listen(port, console.log(
    `Server running on ${port}`
));