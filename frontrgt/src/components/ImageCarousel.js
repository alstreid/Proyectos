import React from 'react';
import { Carousel } from 'react-bootstrap';

import ima1 from "./images/ima1.jpg";
import ima2 from "./images/ima2.jpg";
import ima3 from "./images/ima3.jpg";

const images = [
  { src: ima1, alt: "Imagen 1" },
  { src: ima2, alt: "Imagen 2" },
  { src: ima3, alt: "Imagen 3" },
  // Agrega más imágenes según sea necesario
];

export const ImageCarousel = () => {
    return (
      <div className="d-block w-100">
      <Carousel className="w-100">
        {images.map((image, index) => (
          <Carousel.Item key={index}>
            <img
              className="d-block w-100"
              src={image.src}
              alt={image.alt}
            />
          </Carousel.Item>
        ))}
      </Carousel>
    </div>
    );
  };
  