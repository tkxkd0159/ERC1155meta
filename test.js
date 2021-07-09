const fs = require("fs");

base_meta = {
	"name": "Asset Name",
	"description": "Lorem ipsum...",
	"image": "https:\/\/s3.amazonaws.com\/your-bucket\/images\/{id}.png",
	"properties": {
		"simple_property": "example value",
		"rich_property": {
			"name": "Name",
			"value": "123",
			"display_value": "123 Example Value",
			"class": "emphasis",
			"css": {
				"color": "#ffffff",
				"font-weight": "bold",
				"text-decoration": "underline"
			}
		},
		"array_property": {
			"name": "Name",
			"value": [1,2,3,4],
			"class": "emphasis"
		}
	}
}

path_ = './token/';
file_nums = fs.readdirSync(path_).length;
target_file_number = file_nums.toString(16);
prefix_padding = "0".repeat(64 - target_file_number.length);
next_file_name = `${prefix_padding}${target_file_number}`;
fs.writeFileSync(`${path_}${next_file_name}.json`, JSON.stringify(base_meta));



// fs.writeFileSync("./my.json", JSON.stringify(base_meta))
// testobj = JSON.parse(fs.readFileSync("./my.json"));
// console.log(testobj.properties.array_property.value);