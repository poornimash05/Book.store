import React from 'react'
import { Card } from 'react-bootstrap'
import { Link } from 'react-router-dom'
import Rating from './Rating'
import './ProductCard.css'

function Product({ product }) {
  // 🔧 Ensure image path resolves correctly from `static/images/`
  const imageUrl = product.image?.startsWith('http')
    ? product.image
    : `/images/${product.image?.replace(/^.*[\\/]/, '')}`;  // removes any folders like 'products/' from image name

  return (
    <Card className="my-3 p-3 rounded shadow-sm border-0 book-card h-100">
      <Link to={`/product/${product._id}`}>
        <Card.Img
          src={imageUrl}
          variant="top"
          className="book-img"
          alt={product.name}
        />
      </Link>

      <Card.Body className="d-flex flex-column">
        <Link to={`/product/${product._id}`} className="text-decoration-none">
          <Card.Title as="h5" className="text-dark fw-semibold book-title">
            {product.name.length > 40 ? product.name.slice(0, 40) + '…' : product.name}
          </Card.Title>
        </Link>

        <Card.Text as="div" className="text-muted small">
          {product.category}
        </Card.Text>

        <Card.Text as="div" className="mt-auto">
          <strong>₹{product.price}</strong>
        </Card.Text>

        <Rating value={product.rating} text={`${product.numReviews} reviews`} />
      </Card.Body>
    </Card>
  )
}

export default Product
