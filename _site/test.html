## Others

<strong>Travel & Photography</strong>: Wanderlust fuels my soul, and through the lens, I capture fleeting moments—whispers of light, echoes of time.

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Map with Image Gallery</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
    <script src="https://d3js.org/d3.v6.min.js"></script>
    <style>
        #map { width: 100%; height: 400px; position: relative; z-index: 1; }
        .popup-image {
            width: 30px;
            height: 30px;
            object-fit: cover;
            aspect-ratio: 1/1;
            border-radius: 5px;
            cursor: pointer;
            border: 2px solid white; /* White border */
        }
        .popup-text {
            font-size: 8px;
            font-weight: bold;
            color: black;
            text-shadow: -1px -1px 0 white, 1px -1px 0 white, -1px 1px 0 white, 1px 1px 0 white;
            text-align: center;
            padding: 1px 3px;
            border-radius: 3px;
            position: absolute;
            transform: translateY(-15px) translateX(-32px);
        }
        .popup-text-only {
            font-size: 8px;
            font-weight: bold;
            color: black;
            text-shadow: -1px -1px 0 white, 1px -1px 0 white, -1px 1px 0 white, 1px 1px 0 white;
            text-align: center;
            padding: 1px 3px;
            border-radius: 3px;
            position: absolute;
            transform: translateY(10px) translateX(30px);
        }
        .gallery-popup {
            display: none;
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: rgba(0, 0, 0, 0.8);
            padding: 20px;
            border-radius: 10px;
            z-index: 10000;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
            text-align: center;
        }
        .gallery-popup img {
            max-width: 800px;
            max-height: 800px;
            object-fit: contain;
            border-radius: 10px;
        }
        .close-btn, .prev-btn, .next-btn {
            position: absolute;
            color: white;
            font-size: 20px;
            cursor: pointer;
        }
        .close-btn { top: 10px; right: 20px; }
        .prev-btn { top: 50%; left: 20px; transform: translateY(-50%); }
        .next-btn { top: 50%; right: 20px; transform: translateY(-50%); }
    </style>
</head>
<body>

<div id="map"></div>
<div class="gallery-popup" id="gallery-popup">
    <span class="close-btn" onclick="closeGallery()">×</span>
    <span class="prev-btn" onclick="prevImage()">❮</span>
    <img id="gallery-img" src="" alt="Gallery Image">
    <span class="next-btn" onclick="nextImage()">❯</span>
</div>

<script>
    var map = L.map('map').setView([35, 40], 3.4);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);

    // Mapping non-English names to English
    var countryNameMapping = {
        "États-Unis": "United States of America",
        "Deutschland": "Germany",
        "España": "Spain",
        "Brasil": "Brazil",
        "Россия": "Russia",
        "中国": "China",
        "日本": "Japan",
        "대한민국": "South Korea",
        "المملكة العربية السعودية": "Saudi Arabia",
        "Italia": "Italy",
        "भारत": "India",
        "الإمارات العربية المتحدة": "United Arab Emirates",
        "Türkiye": "Turkey",
        "México": "Mexico",
        "United Kingdom": "United Kingdom", // Already correct
        "France": "France" // Already correct
    };

    // List of visited countries
    var visitedList = {
        "United States of America": ["New York"],
        "France": ["Paris"],
        "China": ["Beijing"],
        "Sri Lanka": ["Colombo", "Mirissa", "Ella", "Kandy", "Galle"],
        "Australia": ["Sydney", "Melbourne"],
        "Mexico": ["Mexico City", "Guanajuato"],
        "Italy": ["Rome", "Venice", "Florence"],
        "Spain": ["Barcelona", "Madrid"],
        "Greece": ["Athens", "Santorini"],
        "Turkey": ["Istanbul"],
        "United Arab Emirates": ["Dubai"],
        "Oman": ["Muscat"],
        "Andorra": ["Andorra la Vella"],
        "Canada": ["Vancouver"],
        "Bahrain": ["Manama"],
        "Austria": ["Vienna"],
        "Hungary": ["Budapest"],
        "Slovakia": ["Bratislava"],
        "Morocco": ["Marrakesh", "Casablanca", "Tangier", "Merzouga", "Chefchaouen", "Fez"],
        "Egypt": ["Cairo", "Luxor", "Aswan"],
        "Saudi Arabia": ["Jeddah"],
        "Switzerland": ["Geneva", "Interlaken"],
        "Vatican City": ["Vatican City"],
        "Vietnam": ["Hanoi"],
    };

    // Load real country borders from GeoJSON (Only draw visited countries)
    fetch("https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json")
        .then(response => response.json())
        .then(data => {
            L.geoJSON(data, {
                filter: function (feature) {
                    let countryName = feature.properties.name;
                    // Convert to English if needed
                    if (countryNameMapping[countryName]) {
                        countryName = countryNameMapping[countryName];
                    }
                    return visitedList.hasOwnProperty(countryName);
                },
                style: function (feature) {
                    return { color: "#008000", weight: 2, fillOpacity: 0.3 };  // Green for visited
                },
                onEachFeature: function (feature, layer) {
                    let countryName = feature.properties.name;
                    // Convert to English if needed
                    if (countryNameMapping[countryName]) {
                        countryName = countryNameMapping[countryName];
                    }
                    layer.bindTooltip(countryName, { permanent: false, direction: "auto" });
                }
            }).addTo(map);
        });

    var cities = [
        // Europe
        { name: "Paris", coords: [48.8566, 2.3522], zoomLevel: 3 },
        { name: "Istanbul", coords: [41.015137, 28.979530], zoomLevel: 2 },
        { name: "Vienna", coords: [48.1236, 16.2148], zoomLevel: 2 },
        { name: "Budapest", coords: [47.497913, 19.040236], zoomLevel: 2 },
        { name: "Bratislava", coords: [48.1486, 17.1077], zoomLevel: 5 },
        { name: "Barcelona", coords: [41.3874, 2.1686], zoomLevel: 2 },
        { name: "Madrid", coords: [40.4167, -3.7033], zoomLevel: 3 },
        { name: "Andorra", coords: [42.5063, 1.5218], zoomLevel: 5 },
        { name: "Athens", coords: [37.9838, 23.7275], zoomLevel: 5 },
        { name: "Santorini", coords: [36.3932, 25.4615], zoomLevel: 2 },
        // America
        { name: "San Francisco", coords: [37.7749, -122.4194], zoomLevel: 2 },
        { name: "Los Angeles", coords: [34.0522, -118.2436], zoomLevel: 2 },
        { name: "New York", coords: [40.7128, -74.0060], zoomLevel: 2 },
        { name: "Boston", coords: [42.3555, -71.0565], zoomLevel: 2 },
        { name: "Philadelphia", coords: [39.9526, -75.1652], zoomLevel: 2 },
        { name: "Mexico City", coords: [19.4326, -99.1332], zoomLevel: 3 },
        { name: "Guanajuato", coords: [21.0190, -101.2574], zoomLevel: 2 },
        { name: "Vancouver", coords: [49.2827, -123.1207], zoomLevel: 2 },
        // China
        { name: "Tibet", coords: [29.6472, 91.1174], zoomLevel: 2 },
        { name: "Sichuan", coords: [30.6509, 104.0757], zoomLevel: 2 },
        { name: "Beijing", coords: [39.9042, 116.4074], zoomLevel: 2 },
        { name: "Fujian", coords: [26.0998, 119.2966], zoomLevel: 2 },
        { name: "Tianjin", coords: [39.0851, 117.1994], zoomLevel: 2 },
        { name: "Hebei", coords: [38.0360, 114.4698], zoomLevel: 2 },
        { name: "Hunan", coords: [28.1142, 112.9833], zoomLevel: 2 },
        { name: "Guangdong", coords: [23.3417, 113.4244], zoomLevel: 2 },
        { name: "Gansu", coords: [36.0594, 103.8263], zoomLevel: 2 },
        { name: "Jilin", coords: [43.8378, 126.5494], zoomLevel: 2 },
        { name: "Liaoning", coords: [41.8357, 123.4291], zoomLevel: 2 },
        { name: "Qinghai", coords: [35.7452, 96.1345], zoomLevel: 2 },
        { name: "Shaanxi", coords: [35.1917, 108.8701], zoomLevel: 2 },
        { name: "Shandong", coords: [36.6683, 117.0204], zoomLevel: 2 },
        { name: "Shanxi", coords: [37.8722, 112.5627], zoomLevel: 2 },
        { name: "Yunnan", coords: [25.0453, 102.7097], zoomLevel: 2 },
        { name: "Shanghai", coords: [31.2304, 121.4737], zoomLevel: 2 },
        { name: "Hong Kong", coords: [22.3193, 114.1694], zoomLevel: 2 },
        // Asia
        { name: "Hanoi", coords: [21.0278, 105.8342], zoomLevel: 2 },
        { name: "Ella", coords: [6.8667, 81.0466], zoomLevel: 3 },
        { name: "Sigiriya", coords: [7.9570, 80.7603], zoomLevel: 2 },
        { name: "Colombo", coords: [6.9271, 79.8612], zoomLevel: 2 },
        { name: "Muscat", coords: [23.5880, 58.3829], zoomLevel: 2 },
        { name: "Jeddah", coords: [21.5292, 39.1611], zoomLevel: 2 },
        // Africa
        { name: "Cairo", coords: [30.0444, 31.2357], zoomLevel: 3 },
        { name: "Aswan", coords: [24.0889, 32.8998], zoomLevel: 2 },
        { name: "Luxor", coords: [25.6872, 32.6396], zoomLevel: 3 },
        { name: "Merzouga", coords: [31.0802, -4.0134], zoomLevel: 2 },
        { name: "Marrakesh", coords: [31.6225, -7.9898], zoomLevel: 5 },
        { name: "Tangier", coords: [35.7595, -5.8340], zoomLevel: 3 },
        { name: "Fez", coords: [34.0181, -5.0078], zoomLevel: 5 },
        { name: "Chefchaouen", coords: [35.1688, -5.2684], zoomLevel: 5 },
        { name: "Casablanca", coords: [33.5731, -7.5898], zoomLevel: 5 },
    ];

    var cityImages = {
        "Paris": [
            "https://story-vl.s3.us-east-1.amazonaws.com/map/paris0.jpg",
            "https://story-vl.s3.us-east-1.amazonaws.com/map/paris1.JPG",
            "https://story-vl.s3.us-east-1.amazonaws.com/map/paris2.JPG"
        ],
        "Istanbul": [
            "https://story-vl.s3.us-east-1.amazonaws.com/map/istanbul0.JPG",
            "https://story-vl.s3.us-east-1.amazonaws.com/map/istanbul1.JPG",
            "https://story-vl.s3.us-east-1.amazonaws.com/map/istanbul2.JPG",
            "https://story-vl.s3.us-east-1.amazonaws.com/map/istanbul3.JPG",
            "https://story-vl.s3.us-east-1.amazonaws.com/map/istanbul4.JPG",
        ],
        "Vienna": [
            "https://story-vl.s3.us-east-1.amazonaws.com/map/vienna0.JPG",
        ],
        "Budapest": [
            "https://story-vl.s3.us-east-1.amazonaws.com/map/budapest0.JPG",
            "https://story-vl.s3.us-east-1.amazonaws.com/map/budapest1.jpg"
        ],
        "Barcelona": [
            "https://story-vl.s3.us-east-1.amazonaws.com/map/barcelona0.JPG",
            "https://story-vl.s3.us-east-1.amazonaws.com/map/barcelona1.JPG",
            "https://story-vl.s3.us-east-1.amazonaws.com/map/barcelona2.JPG",
            "https://story-vl.s3.us-east-1.amazonaws.com/map/barcelona3.JPG",
            "https://story-vl.s3.us-east-1.amazonaws.com/map/barcelona4.JPG",
        ],
        "Madrid": [
            "https://story-vl.s3.us-east-1.amazonaws.com/map/madrid0.JPG",
        ],
        "Muscat": [
            "https://story-vl.s3.us-east-1.amazonaws.com/map/muscat0.JPG",
        ],
        "Andorra": [
            "https://story-vl.s3.us-east-1.amazonaws.com/map/andorra0.JPG",
        ],
        "Athens": [
            "https://story-vl.s3.us-east-1.amazonaws.com/map/athens0.JPG",
            "https://story-vl.s3.us-east-1.amazonaws.com/map/athens1.JPG",
        ],
        "Santorini": [
            "https://story-vl.s3.us-east-1.amazonaws.com/map/santorini0.JPG",
            "https://story-vl.s3.us-east-1.amazonaws.com/map/santorini1.JPG",
        ],
        "Vancouver": [
           "https://story-vl.s3.us-east-1.amazonaws.com/map/vancouver0.JPG",
           "https://story-vl.s3.us-east-1.amazonaws.com/map/vancouver1.JPG",
           "https://story-vl.s3.us-east-1.amazonaws.com/map/vancouver2.JPG",
        ],
        "Tibet": [
            "https://story-vl.s3.us-east-1.amazonaws.com/map/tibet1.JPG",
            "https://story-vl.s3.us-east-1.amazonaws.com/map/tibet0.JPG",
        ],
        "Sichuan": [
            "https://story-vl.s3.us-east-1.amazonaws.com/map/sichuan0.JPG",
            "https://story-vl.s3.us-east-1.amazonaws.com/map/sichuan1.JPG",
        ],
        "Hanoi": [
            "https://story-vl.s3.us-east-1.amazonaws.com/map/hanoi1.JPG",
            "https://story-vl.s3.us-east-1.amazonaws.com/map/hanoi2.JPG",
            "https://story-vl.s3.us-east-1.amazonaws.com/map/hanoi3.JPG",
        ],
        "Merzouga": [
            "https://story-vl.s3.us-east-1.amazonaws.com/map/merzouga0.JPG",
        ],
        "Marrakesh": [
            "https://story-vl.s3.us-east-1.amazonaws.com/map/marrakesh0.jpg",
        ],
        "Tangier": [
            "https://story-vl.s3.us-east-1.amazonaws.com/map/tangier0.JPG",
            "https://story-vl.s3.us-east-1.amazonaws.com/map/tangier1.JPG",
        ],
        "Fez": [
            "https://story-vl.s3.us-east-1.amazonaws.com/map/fes0.JPG",
        ],
        "Chefchaouen": [
            "https://story-vl.s3.us-east-1.amazonaws.com/map/chefchaouen0.JPG",
            "https://story-vl.s3.us-east-1.amazonaws.com/map/chefchaouen1.JPG",
        ],
    };

    var currentCity = "";
    var currentImageIndex = 0;

    function openGallery(city) {
        if (cityImages[city]) {
            currentCity = city;
            currentImageIndex = 0;
            document.getElementById("gallery-img").src = cityImages[city][currentImageIndex];
            document.getElementById("gallery-popup").style.display = "block";
        }
    }

    function closeGallery() {
        document.getElementById("gallery-popup").style.display = "none";
    }

    function nextImage() {
        if (currentCity && cityImages[currentCity]) {
            currentImageIndex = (currentImageIndex + 1) % cityImages[currentCity].length;
            document.getElementById("gallery-img").src = cityImages[currentCity][currentImageIndex];
        }
    }

    function prevImage() {
        if (currentCity && cityImages[currentCity]) {
            currentImageIndex = (currentImageIndex - 1 + cityImages[currentCity].length) % cityImages[currentCity].length;
            document.getElementById("gallery-img").src = cityImages[currentCity][currentImageIndex];
        }
    }

    var markers = [];

    function updateCityMarkers() {
        markers.forEach(marker => map.removeLayer(marker)); // Remove old markers
        markers = [];

        var currentZoom = map.getZoom();

        cities.forEach(city => {
            if (currentZoom >= city.zoomLevel){
                if (cityImages.hasOwnProperty(city.name) && cityImages[city.name].length > 0) {
                    var icon = L.divIcon({
                        className: "custom-icon",
                        html: `<div class='custom-popup'>
                                  <img class='popup-image' src='${cityImages[city.name][0]}' data-city='${city.name}' />
                                  <span class='popup-text'>${city.name}</span>
                               </div>`,
                        iconSize: [100, 100],
                        iconAnchor: [50, 20]
                    });
                }
                else{
                    var icon = L.divIcon({
                        className: "custom-icon",
                        html: `<div class='custom-popup'>
                                  <span class='popup-text-only'>${city.name}</span>
                               </div>`,
                        iconSize: [100, 100],
                        iconAnchor: [50, 20]
                    });
                }
                var marker = L.marker(city.coords, {icon: icon}).addTo(map);
                markers.push(marker);
            }
        });
    }

    map.on("zoomend", updateCityMarkers);
    updateCityMarkers();

    document.body.addEventListener("click", function (event) {
        if (event.target.classList.contains("popup-image")) {
            var city = event.target.getAttribute("data-city");
            openGallery(city);
        }
    });

</script>

</body>
</html>

