import 'package:attendance_project_slave/Login.dart';
import 'package:attendance_project_slave/SignUp.dart';
import 'package:attendance_project_slave/UserName.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(
    MaterialApp(
      debugShowCheckedModeBanner: false,
      initialRoute: 'Login',
      routes: {
        'Login': (context) => Login(),
        'SignUp': (context)=> SignUp(),
        'UserName': (context)=> UserName(),
      },
    ),
  );
}
