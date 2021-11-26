# JsonToYaml

This is a little python script that I used to convert a large json array into a markdown/toml file. Created this because I was using the netlify cms to manage content on my website but It only accepted markdown files so ... yea.
Script is just a simple for loop so feel free to use it. I might refactor it later so that it could become a cli tool which accepts input and output file as an argument :/.

How to use:

paste your json array into the `array.json` file <br/>

Edit the following variables 
```python
file_title = "Menu"
data_title = "menu_item"
file_body = "This is the menu page for the Flamingo Restaurant Website"
```

Thats it. Run it and you will get an output file with the `{file_title}.md` as its name. For me, it was -> `menu.md`


Have fun 😊
