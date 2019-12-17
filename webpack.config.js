require('dotenv/config');
// https://medium.com/labcodes/configurando-um-projeto-django-com-react-1292abded7a5
const path = require('path');
let CopyWebpackPlugin = require('copy-webpack-plugin');


module.exports = (env, argv) => {

    let copyStaticToDir = process.env.STATIC_DIR;
    if (argv.mode == 'development') {
        copyStaticToDir = process.env.STATIC_ROOT
    }
    // TODO: https://www.youtube.com/watch?v=A2vEazcfJ7U
    config = {
        mode: argv.mode,
        entry: './src/index.js',
        output: {
            publicPath: 'http://127.0.0.1:8099/'
        },
        devServer: {
            headers: {
                'Access-Control-Allow-Origin': '*'
            }
        },
        plugins: [
            new CopyWebpackPlugin([{
                from: './node_modules/admin-lte',
                to: path.resolve(__dirname, path.join(copyStaticToDir, 'admin-lte'))
            }]),
            new CopyWebpackPlugin([{
                from: './node_modules/select2/dist/js',
                to: path.resolve(__dirname, path.join(copyStaticToDir, 'select2/js'))
            }]),
            new CopyWebpackPlugin([{
                from: './node_modules/select2/dist/css',
                to: path.resolve(__dirname, path.join(copyStaticToDir, 'select2/css'))
            }]),
            new CopyWebpackPlugin([{
                from: './node_modules/select2-bootstrap-theme/dist',
                to: path.resolve(__dirname, path.join(copyStaticToDir, 'select2/css'))
            }])
        ]
    }

    return config
};
