// var gulp = require('gulp');

// gulp.task('info', function() {
//   // 将你的默认的任务代码放在这
//   console.log('hello world');
// });

var gulp = require('gulp'),
	uglify = require('gulp-uglify'),
	rename = require('gulp-rename'),	// 4、给gulp重命名
	less = require('gulp-less'), // 1、导入less模块
	cssmin = require('gulp-minify-css'), // 3、css压缩
	prefix = require('gulp-autoprefixer'); // 2、给css3加前缀







gulp.task('less',function(){
	gulp.src('src/css/*.less') 
	.pipe(less())
	.pipe(prefix())
	// .pipe(cssmin()) 不压缩
	.pipe(rename({suffix:'.min'}))
	.pipe(gulp.dest('dist/css/'))

	// 去查找 src下面的css文件的 包含.less文件
	// 放到dist上的css文件里面
	// src是开发目录
	// dist是最终输出的目录（上线的目录）
})