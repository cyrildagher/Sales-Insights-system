'use client';
import { useEffect, useState } from "react";
import InsightCard from "@/components/InsightCard";
import { FaBox, FaDollarSign, FaMapMarkerAlt, FaArrowRight } from "react-icons/fa";

type ProductInsight = {
  product_name: string;
  total_revenue: number;
  top_region: string;
};

export default function Home() {
  const [productInsights, setProductInsights] = useState<ProductInsight[]>([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function fetchInsights() {
      try {
        // Fetch top products
        const productsRes = await fetch("http://localhost:8000/api/top-products");
        const products = await productsRes.json();

        // For each product, fetch its top region and total sales (this month)
        const insights: ProductInsight[] = await Promise.all(
          products.map(async (product: any) => {
            // Fetch total sales for this product (this month)
            const salesRes = await fetch(
              `http://localhost:8000/api/monthly-sales?product=${encodeURIComponent(product.product_name)}`
            );
            const sales = await salesRes.json();
            // Get the latest month sales for this product
            const latestMonth = sales.length > 0 ? sales[sales.length - 1].total_revenue : 0;

            // Fetch top region for this product
            const regionRes = await fetch(
              `http://localhost:8000/api/sales-by-region?product=${encodeURIComponent(product.product_name)}`
            );
            const regions = await regionRes.json();
            const topRegion = regions.length > 0 ? regions[0].region : "N/A";

            return {
              product_name: product.product_name,
              total_revenue: latestMonth,
              top_region: topRegion,
            };
          })
        );

        setProductInsights(insights);
      } catch (err) {
        setError("Failed to fetch insights.");
      } finally {
        setLoading(false);
      }
    }
    fetchInsights();
  }, []);

  const handleNext = () => {
    setCurrentIndex((prev) =>
      productInsights.length === 0 ? 0 : (prev + 1) % productInsights.length
    );
  };

  const current = productInsights[currentIndex];

  return (
    <main className="p-8 space-y-8 max-w-5xl mx-auto">
      <div className="mb-4">
        <h1 className="text-4xl font-extrabold mb-2">Sales Insights Dashboard</h1>
        <p className="text-gray-600 text-lg">Cycle through your top products and their key metrics</p>
      </div>
      {loading ? (
        <div>Loading...</div>
      ) : error ? (
        <div className="text-red-500">{error}</div>
      ) : current ? (
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 relative">
          <InsightCard
            title="Top Product"
            value={current.product_name}
            icon={<FaBox size={28} />}
          />
          <InsightCard
            title="Total Sales (This Month)"
            value={`$${Number(current.total_revenue).toLocaleString()}`}
            icon={<FaDollarSign size={28} />}
          />
          <InsightCard
            title="Top Region"
            value={current.top_region}
            icon={<FaMapMarkerAlt size={28} />}
          />
          {productInsights.length > 1 && (
            <button
              onClick={handleNext}
              className="absolute -bottom-12 left-1/2 transform -translate-x-1/2 bg-blue-500 hover:bg-blue-600 text-white rounded-full p-3 transition"
              title="Next Product"
            >
              <FaArrowRight size={20} />
            </button>
          )}
        </div>
      ) : (
        <div>No data available.</div>
      )}
    </main>
  );
}