var path = require('path')
var webpack = require('webpack')

module.exports = {
    context: __dirname,
    mode: 'development',
    entry: './front/main.jsx',

    output: {
        path: path.resolve('./static'),
        filename: 'bundle.js',
    },

    module: {
        rules: [
            {
                test: /\.jsx?$/,
                //exclude: /node_modules/,
                loader: 'babel-loader',
                query: {
                    presets: ['react', 'es2015']
                }
            },
            {
                test: /\.css$/,
                use: [ 'style-loader', 'css-loader' ]
            }
        ]
    },

    resolve: {
        //extensions that should be used to resolve modules
        extensions: ['.js', '.jsx', '.css'],
    }
}
