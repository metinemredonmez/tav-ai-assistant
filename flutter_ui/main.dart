
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'TAV AI Assistant',
      home: Scaffold(
        appBar: AppBar(title: Text('TAV AI Assistant')),
        body: AIForm(),
      ),
    );
  }
}

class AIForm extends StatefulWidget {
  @override
  _AIFormState createState() => _AIFormState();
}

class _AIFormState extends State<AIForm> {
  final _controller = TextEditingController();
  String _response = '';

  void _askQuestion() async {
    final question = _controller.text;
    final res = await http.post(
      Uri.parse('http://10.0.2.2:8000/ask'),  // Adjust for emulator or device
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'question': question}),
    );
    final data = jsonDecode(res.body);
    setState(() {
      _response = data['response'];
    });
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        TextField(controller: _controller),
        ElevatedButton(onPressed: _askQuestion, child: Text('Gönder')),
        SizedBox(height: 20),
        Text('Yanıt: $_response'),
      ],
    );
  }
}
