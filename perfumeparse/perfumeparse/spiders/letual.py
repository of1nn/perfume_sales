import re

import scrapy
from perfumeparse.items import PerfumeparseItem


class LetualSpider(scrapy.Spider):
    name = 'letual'
    allowed_domains = [
        'letu.ru/browse/muzhchinam/muzhskaya-parfyumeriya'
    ]
    start_urls = [
        'https://www.letu.ru/browse/muzhchinam/muzhskaya-parfyumeriya/'
    ]

    def parse(self, response):
        all_perfume = response.css('.product-tile__item-container')
        for perfume_link in all_perfume:
            yield response.follow(perfume_link, callback=parse_perfume)

    def parse_perfume(self, response):
        data = {
            name: response.css(
                '#content-wrap > div.container.product-main-info.product-main-info_detail-page > div > div > div > div.product-detail > div.row > div.product-detail-sku-header.product-detail__sku-header.col-xs-12.col-first-sm > div.product-detail-sku-header__info-block.row.row-between-xs > div.product-detail-sku-header__left-block > div > h1::text'
            ).get(),
            price: re.findall(
                '\d+',
                response.css(
                    '.product-detail-price__base-price .product-detail-price__base-price--new-design::text'
                ).get(),
            )[0],
            valume: re.findall(
                '\d+',
                response.css(
                    '.product-detail-sku-volume__label:first-child::text'
                ),
            ),
            image: 'letu.ru/'
            + response.css(
                '.product-detail-media-carousel__horizontal-item img:first:attr(src)'
            ).get(),
            type: response.css(
                '#content-wrap > div.container.product-main-info.product-main-info_detail-page > div > div > div > div.product-detail > div.row > div.product-detail-sku.col-xs-12.col-sm-6.col-md-7 > div > div.top-characteristics.top-characteristics--second-column > div:nth-child(1) > div:nth-child(2) > span'
            )
            .get()
            .strip(),
            aromas: response.css(
                '.top-characteristics__text.top-characteristics__text--right::text'
            ),
            url: response.request.url,
        }
        yield PerfumeparseItem(data)
