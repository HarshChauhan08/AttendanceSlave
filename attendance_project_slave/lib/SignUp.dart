import 'package:flutter/material.dart';

class SignUp extends StatefulWidget {
  const SignUp({Key? key}) : super(key: key);

  @override
  _SignUpState createState() => _SignUpState();
}

class _SignUpState extends State<SignUp> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        body: SafeArea(
          child: Stack(
            children: [
              SingleChildScrollView(
                child: Container(
                  padding: EdgeInsets.only(top: 20, left: 30),
                  child: Text(
                    "Create Account",
                    style: TextStyle(color: Colors.deepPurple[300], fontSize: 33),
                  ),
                  color: Colors.transparent,
                ),
              ),
              SingleChildScrollView(
                child: Container(
                  padding: EdgeInsets.only(top: 105, left: 35, right: 50),
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
                        decoration: InputDecoration(
                            hintText: 'Name',
                            border: OutlineInputBorder(
                                borderRadius: BorderRadius.circular(12))),
                      ),
                      SizedBox(
                        height: 30,
                      ),
                      TextField(
                        keyboardType: TextInputType.number,
                        decoration: InputDecoration(
                            hintText: 'PRN',
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
                        height: 30,
                      ),
                      // Password
                      TextField(
                        obscureText: true,
                        decoration: InputDecoration(
                            hintText: 'Confirm Password',
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
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          TextButton(
                            onPressed: () {
                              Navigator.pushNamed(context, 'Login');
                            },
                            child: Text(
                              "Log in",
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
