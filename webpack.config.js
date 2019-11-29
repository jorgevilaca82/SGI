require('dotenv/config');
// https://medium.com/labcodes/configurando-um-projeto-django-com-react-1292abded7a5
const path = require('path');
let CopyWebpackPlugin = require('copy-webpack-plugin');


module.exports = (env, argv) => {

    let copyStaticToDir = process.env.STATIC_DIR;
    if (argv.mode == 'development') {
        copyStaticToDir = process.env.STATIC_ROOT
    }

    config = {
        entry: './index.js',
        plugins: [
            new CopyWebpackPlugin([{
                from: './node_modules/admin-lte',
                to: path.resolve(__dirname, path.join(copyStaticToDir, 'admin-lte'))
            }])
        ]
    }

    return config
};
