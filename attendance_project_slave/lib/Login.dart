import 'package:attendance_project_slave/SignUp.dart';
import 'package:flutter/material.dart';

class Login extends StatefulWidget {
  const Login({Key? key}) : super(key: key);

  @override
  _LoginState createState() => _LoginState();
}

class _LoginState extends State<Login>  {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        body: SafeArea(
          child: Stack(
            children: [
              Container(
                padding: EdgeInsets.only(top: 120, left: 50),
                child: Text(
                  "Welcome!\nGood to see you",
                  style: TextStyle(color: Colors.deepPurple[300], fontSize: 33),
                ),
                color: Colors.transparent,
              ),
              SingleChildScrollView(
                child: Container(
                  padding: EdgeInsets.only(top: 295, left: 35, right: 50),
                  child: Column(
                    children: [
                      // EmailBox
                      TextField(
                        decoration: InputDecoration(
                            hintText: 'Email',
                            border: OutlineInputBorder(
                                borderRadius: BorderRadius.circular(12))),
                      ),
                      // GapBetweenBox
                      SizedBox(
                        height: 30,
                      ),
                      // Password
                      TextField(
                        obscureText: true,
                        decoration: InputDecoration(
                            hintText: 'Password',
                            border: OutlineInputBorder(
                                borderRadius: BorderRadius.circular(12))),
                      ),
                      SizedBox(
                        height: 25,
                      ),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Text(
                            "Sign in",
                            style: TextStyle(fontSize: 25),
                          ),
                          CircleAvatar(
                            radius: 25,
                            backgroundColor: Colors.deepPurple[200],
                            child: IconButton(
                              color: Colors.white,
                              icon: Icon(Icons.arrow_forward_outlined),
                              onPressed: () {},
                            ),
                          ),
                        ],
                      ),
                      SizedBox(
                        height: 25,
                      ),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          TextButton(
                            onPressed: () {
                              Navigator.pushNamed(context, 'SignUp');
                            },
                            child: Text(
                              "Sign Up?",
                              style: TextStyle(
                                  decoration: TextDecoration.underline,
                                  fontSize: 18,
                                  color: Colors.deepPurple[300]),
                            ),
                          ),
                          TextButton(
                            onPressed: () {},
                            child: Text(
                              "Forgot Password?",
                              style: TextStyle(
                                  decoration: TextDecoration.underline,
                                  fontSize: 18,
                                  color: Colors.deepPurple[300]),
                            ),
                          )
                        ],
                      ),
                      SizedBox(
                        height: 25,
                      ),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          TextButton(
                            onPressed: () {
                              Navigator.pushNamed(context, 'UserName');
                            },
                            child: Text(
                              "View User Name",
                              style: TextStyle(
                                  decoration: TextDecoration.underline,
                                  fontSize: 18,
                                  color: Colors.deepPurple[300]),
                            ),
                          ),
                        ],
                      ),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}


