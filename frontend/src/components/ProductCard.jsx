export default function ProductCard({ product }) {
  return (
    <div className="border p-4 rounded shadow-md">
      <h2 className="text-xl font-bold">{product.name}</h2>
      <p>Preço: R$ {product.price}</p>
      <p>Categoria: {product.category_id}</p>
    </div>
  );
}
