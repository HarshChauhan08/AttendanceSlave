import 'package:flutter/material.dart';
import 'package:attendance_project_slave/Student.dart';

class UserName extends StatefulWidget {
  const UserName({Key? key}) : super(key: key);

  @override
  _UserNameState createState() => _UserNameState();
}

class _UserNameState extends State<UserName> {
  Student studentService = Student();
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        body: SafeArea(
          child: Stack(
            children: [
              Container(
                padding: EdgeInsets.only(top: 40, left: 20, right: 20),
                child: Text(
                  "Below Data Is Taken From Database",
                  style: TextStyle(color: Colors.deepPurple[300], fontSize: 33),
                ),
                color: Colors.transparent,
              ),
              Container(
                padding: EdgeInsets.only(top: 150, left: 0, right: 20),
                child: FutureBuilder<List>(
                  future: studentService.getAllStudent(),
                  builder: (context, data) {
                    print(context);
                    if(data.hasData){
                      return ListView.builder(
                          itemCount: data.data?.length,
                          itemBuilder: (context, i) {
                            return Card(
                              child: ListTile(
                                title: Text(
                                  data.data![i]['studentEmail'],
                                  style: TextStyle(fontSize: 20),
                                ),
                                subtitle: Text(
                                  data.data![i]['studentPassword'],
                                  style: TextStyle(fontSize: 20),
                                ),
                              ),
                            );
                          });
                    }
                    else{
                      return const Center(
                        child: Text("No Data"),
                      );
                    }
                  }),
                )
              ],
          ),
        ),
      ),
    );
  }
}
