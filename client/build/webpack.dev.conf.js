const utils = require('./utils')
const webpack = require('webpack')
const config = require('../config')
const merge = require('webpack-merge')
const path = require('path')
const fs = require('fs-extra')
const CleanWebpackPlugin = require('clean-webpack-plugin')
const baseWebpackConfig = require('./webpack.base.conf')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const FriendlyErrorsPlugin = require('friendly-errors-webpack-plugin')
const WebpackOnBuildPlugin = require('on-build-webpack')

function resolve (dir) {
  return path.join(__dirname, '..', dir)
}

let pathsToClean = [
  'dev'
]

// the clean options to use
let cleanOptions = {
  root: resolve('/'),
  exclude: ['shared.js'],
  verbose: true,
  dry: false
}

// add hot-reload related code to entry chunks
Object.keys(baseWebpackConfig.entry).forEach(function (name) {
  baseWebpackConfig.entry[name] = ['./build/dev-client'].concat(baseWebpackConfig.entry[name])
})

module.exports = merge(baseWebpackConfig, {
  module: {
    rules: utils.styleLoaders({ sourceMap: config.dev.cssSourceMap })
  },
  // watch for file changes
  watch: true,
  // cheap-module-eval-source-map is faster for development
  devtool: 'cheap-module-eval-source-map',
  plugins: [
    // new webpack.HotModuleReplacementPlugin(),
    new webpack.NoEmitOnErrorsPlugin(),
    new CleanWebpackPlugin(pathsToClean, cleanOptions),
    new HtmlWebpackPlugin({
      filename: 'index.html',
      template: 'index.html',
      inject: true
    }),
    new FriendlyErrorsPlugin(),
    new WebpackOnBuildPlugin(function (stats) {
      let jsFiles = []

      let jsDir = path.resolve(__dirname, '..', '..', 'app', 'static')

      try {
        fs.readdir(path.resolve(__dirname, '..', 'dev'), function (err, list) {
          if (err) {
            throw err
          }

          jsFiles = list.filter(utils.filterExtension, {'ext': 'js'})

          function addPath (file) {
            return path.resolve(__dirname, '..', 'dev') + '/' + file
          }

          jsFiles = jsFiles.map(addPath)

          utils.copyFilesToDir(jsFiles, jsDir)
        })
      } catch (err) {
        console.error(err)
      }
    })
  ]
})
